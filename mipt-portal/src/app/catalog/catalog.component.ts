import {Component, OnInit} from '@angular/core';

export interface CatalogItem {
  pictureUrl: string;
  name: string;
  description: string;
}


const CATALOG: CatalogItem[] = [
  {
    pictureUrl: '/assets/images/user_activity.png',
    name: 'Airport Load',
    description: 'This is a demo application for MIPT course on development of aviation analytical software. Shows current load with passengers in any airport'
  },
  // {
  //   pictureUrl: '/assets/images/user_activity.png',
  //   name: 'User Activity',
  //   description: 'This is a demo application for MIPT course on development of aviation analytical software. Shows statistics of portal usage by each user'
  // },
  // {
  //   pictureUrl: '/assets/images/user_activity.png',
  //   name: 'User Activity',
  //   description: 'This is a demo application for MIPT course on development of aviation analytical software. Shows statistics of portal usage by each user'
  // },
  // {
  //   pictureUrl: '/assets/images/user_activity.png',
  //   name: 'User Activity',
  //   description: 'This is a demo application for MIPT course on development of aviation analytical software. Shows statistics of portal usage by each user'
  // },
  // {
  //   pictureUrl: '/assets/images/user_activity.png',
  //   name: 'User Activity',
  //   description: 'This is a demo application for MIPT course on development of aviation analytical software. Shows statistics of portal usage by each user'
  // },  {
  //   pictureUrl: '/assets/images/user_activity.png',
  //   name: 'User Activity',
  //   description: 'This is a demo application for MIPT course on development of aviation analytical software. Shows statistics of portal usage by each user'
  // },

];


@Component({
  selector: 'app-catalog',
  templateUrl: './catalog.component.html',
  styleUrls: ['./catalog.component.scss']
})
export class CatalogComponent implements OnInit {
  catalog = CATALOG;

  constructor() {
  }

  ngOnInit(): void {
  }

}
