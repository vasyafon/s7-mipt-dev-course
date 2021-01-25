import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AirportLoadComponent } from './airport-load.component';

describe('AirportLoadComponent', () => {
  let component: AirportLoadComponent;
  let fixture: ComponentFixture<AirportLoadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AirportLoadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AirportLoadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
