import { Component, ElementRef, EventEmitter, Input, Output, ViewChild } from '@angular/core';
import { ImageRecognizerService } from 'src/app/image-recognizer/services/image-recognizer.service';

@Component({
  selector: 'app-condicion',
  templateUrl: './condicion.component.html'
})
export class CondicionComponent {

  @Input() public siguienteBloque: string = "";
  @Input() public condicion: string = "";

  @Output() modificaCondicion = new EventEmitter<{[id: string]: string}>();

  @ViewChild("condicionBloque") condicionBloque!: ElementRef<HTMLInputElement>;

  get isServiceWorking() { return this.imageRecognizerService.isworking; }

  constructor(private imageRecognizerService: ImageRecognizerService) { }

  cambiarCondicion(): void {
    this.condicion = this.condicionBloque.nativeElement.value;
    let cond: {[id: string]: string} = {
      'siguienteBloque': this.siguienteBloque,
      'condicion': this.condicion
    }
    this.modificaCondicion.emit(cond);
  }
}
