import { Component } from '@angular/core';
import { ImageRecognizerService } from '../services/image-recognizer.service';

@Component({
  selector: 'app-recognizer',
  templateUrl: './recognizer.component.html'
})
export class RecognizerComponent {

  
  constructor(private imageRecognizerService: ImageRecognizerService) { }

}
