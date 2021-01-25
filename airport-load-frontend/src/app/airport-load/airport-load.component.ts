import {AfterViewInit, Component, OnDestroy, OnInit, ViewEncapsulation} from '@angular/core';
import {ApiService} from '../api/api.service';
import * as d3 from 'd3';
import * as d3Geo from 'd3-geo';
import * as d3Tip from 'd3-tip';
import * as topojson from 'topojson-client';
import {BriefAirportLoadInfo, GlobalLoadInfo} from '../../clients/airport-load';
import {GeoPath} from 'd3-geo';
import {Subscription, timer} from 'rxjs';


@Component({
  selector: 'app-airport-load',
  templateUrl: './airport-load.component.html',
  styleUrls: ['./airport-load.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class AirportLoadComponent implements OnInit, AfterViewInit, OnDestroy {
  public maxCanvasWidth = '100%';
  public svgId = 'A';
  private svg: any;
  private g: any;
  private drawWidth: number;
  private drawHeight: number;
  private width: number;
  private height: number;
  private margin = {top: 0, right: 0, bottom: 0, left: 0};
  private projection: any;
  private globalInfo: BriefAirportLoadInfo[];
  private airportBalls: any;
  private path: GeoPath;
  private tip: any;
  private tooltip: any;
  private offsetL: number;
  private offsetT: number;
  private timerSubscription: Subscription;

  constructor(private api: ApiService) {
  }

  ngOnInit(): void {
  }

  ngAfterViewInit(): void {
    this.initSVG();
    this.updateContours();
    this.timerSubscription = timer(0, 10000).subscribe(() => {
      this.fetchGlobalData();
    });
  }

  ngOnDestroy() {
    if (this.timerSubscription) {
      this.timerSubscription.unsubscribe();
    }

  }

  private initSVG(): void {
    this.drawWidth = 1920;
    this.drawHeight = 1080;
    this.width = this.drawWidth - this.margin.left - this.margin.right;
    this.height = this.drawHeight - this.margin.top - this.margin.bottom;

    // this.tooltip = d3.select('div#container-load' + this.svgId)
    //   .append('div')
    //   .attr('class', 'tooltip');

    this.svg = d3.select('div#container-load' + this.svgId)
      .append('svg')
      .attr('viewBox', `0 0  ${this.drawWidth} ${this.drawHeight}`)
      .classed('svg-content', true)
      .attr('preserveAspectRatio', 'xMinYMin meet')
      .classed('svg-content-responsive', true);
    this.g = this.svg.append('g');

    this.svg.call(d3.zoom().on('zoom', () => {
      this.g
        .attr('transform', d3.event.transform);
    }));

    this.projection = d3Geo.geoMercator()
      .scale(600)
      .translate([700, 1400])
      .rotate([-90, 0, 0]);
    this.path = d3Geo.geoPath(this.projection);

    this.tip = d3Tip.default()
      .attr('class', 'd3-tip')
      .offset([-10, 0])
      .html((d) => {
        return d.airportCode + ': ' + (d.paxLoad);
      });
    this.g.call(this.tip);
  }

  private updateContours(): void {
    d3.json('assets/topo/countries-110m.json').then((world: any) => {
      const features = topojson.feature(world, world.objects.countries) as any;
      this.g.append('g')
        .attr('class', 'boundary')
        .selectAll('boundary')
        .data(features.features)
        .enter().append('path')
        .attr('d', this.path);


    });
  }

  private updateAirports(): void {
    this.g.selectAll('.airportBalls').remove();
    this.airportBalls = this.g.selectAll('.airportBalls')
      .data(this.globalInfo.filter(d => d.latitude != null && d.longititude != null && d.paxLoad != null))
      .enter()
      .append('g')
      .attr('transform', (d) => `translate(${this.projection([d.longititude, d.latitude])}) `);

    this.airportBalls.append('circle')
      .attr('r', d => Math.log(d.paxLoad + 1) + 2.5)
      .style('fill', '#bed100')
      .on('mouseover', (d, index, element) => this.tip.show(d, element[index]))
      .on('mouseout', () => this.tip.hide());

    this.airportBalls.append('text')
      .text(d => d.airportCode)
      .attr('font-size', 5)
      .attr('dy', d => Math.log(d.paxLoad + 1) + 2 + 7)
      .attr('text-anchor', 'middle')
      .style('fill', '#FFFFFF')
      .style('stroke', 'black')
      .style('stroke-width', '0.6')
      .style('paint-order', 'stroke');

    this.airportBalls.append('text')
      .text(d => d.paxLoad)
      .attr('font-size', 5)
      .attr('dy', 2.5)
      .attr('text-anchor', 'middle')
      .style('fill', 'black')
      .style('stroke', 'v')
      .style('stroke-width', '0.6')
      .style('paint-order', 'stroke');

  }

  private fetchGlobalData(): void {
    this.api.globalService.getGlobalInfo().subscribe(info => {
      this.globalInfo = info.data;
      this.updateAirports();
    });

  }
}

