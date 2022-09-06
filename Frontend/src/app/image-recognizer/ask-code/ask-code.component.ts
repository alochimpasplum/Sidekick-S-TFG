import { Component } from '@angular/core';
import { ImageRecognizerService } from '../services/image-recognizer.service';

@Component({
  selector: 'app-ask-code',
  templateUrl: './ask-code.component.html'
})
export class AskCodeComponent {
  
  public languajes: string[] = [];

  get serverLanguajes() { return this.imageRecognizerService.serverLanguajes; }
  get isServiceWorking() { return this.imageRecognizerService.isworking; }
  get mermaidBlocks() { return this.imageRecognizerService.mermaidBlocks; }

  constructor(private imageRecognizerService: ImageRecognizerService) {}

  onCheckboxChange(event: any) : void {
    if(event.target.checked) {
      if(!this.languajes.includes(event.target.value))
        this.languajes.push(event.target.value)
    } else {
      if(this.languajes.includes(event.target.value)){
        let index: number = this.languajes.indexOf(event.target.value);
        this.languajes.splice(index, 1);
      }
    }
  }

  getCode(): void {
    this.imageRecognizerService.getCode(this.languajes);
  }
}
