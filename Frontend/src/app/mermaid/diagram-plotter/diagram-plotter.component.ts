import { Component } from '@angular/core';
import { ImageRecognizerService } from 'src/app/image-recognizer/services/image-recognizer.service';

@Component({
  selector: 'app-diagram-plotter',
  templateUrl: './diagram-plotter.component.html'
})
export class DiagramPlotterComponent {

  get mermaidReady() { return this.imageRecognizerService.mermaidReady; }
  get mermaidUrl() { return this.imageRecognizerService.urlImagenMermaid; }
  get mermaidBlocks() { return this.imageRecognizerService.mermaidBlocks; }
  get isMermaidBlocksChanges() { return this.imageRecognizerService.isMermaidBlocksChanges; }
  get isServiceWorking() { return this.imageRecognizerService.isworking; }

  constructor (private imageRecognizerService: ImageRecognizerService) { }

  public subeCambiosMermaid(): void {
    this.imageRecognizerService.modifyMermaidDiagram();
  }
}