import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DiagramPlotterComponent } from './diagram-plotter/diagram-plotter.component';
import { BlockComponent } from './block/block.component';
import { CondicionComponent } from './block/condicion/condicion.component';


@NgModule({
  declarations: [
    DiagramPlotterComponent,
    BlockComponent,
    CondicionComponent
  ],
  exports: [
    DiagramPlotterComponent
  ],
  imports: [
    CommonModule
  ]
})
export class MermaidModule { }
