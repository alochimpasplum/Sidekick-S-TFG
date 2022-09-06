import { Component, ElementRef, Input, ViewChild } from '@angular/core';
import { ImageRecognizerService } from 'src/app/image-recognizer/services/image-recognizer.service';
import { MermaidBlock } from 'src/app/interfaces/getMermaidFromImage.interface';

@Component({
  selector: 'app-block',
  templateUrl: './block.component.html'
})
export class BlockComponent {

  @ViewChild("textoBloque") textoBloque!: ElementRef<HTMLInputElement>;

  @Input() public block: MermaidBlock = {
    block_name: "",
    text: "",
    previous_blocks: [],
    next_blocks: [],
    next_blocks_conditionals: {},
    object_type: ""
  }

  get isServiceWorking() { return this.imageRecognizerService.isworking; }

  constructor(private imageRecognizerService: ImageRecognizerService) { }

  cambiarTexto(): void {
    this.block.text = this.textoBloque.nativeElement.value;
    this.realizaConsulta();
  }

  modificaCondicion(_event: {[id: string]: string}): void {
    this.block.next_blocks_conditionals[_event['siguienteBloque']] = _event['condicion'];
    this.realizaConsulta();
  }

  private realizaConsulta(): void {
    this.imageRecognizerService.modifyMermaidBlocks(this.block);
  }

}