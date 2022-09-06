import { Component } from '@angular/core';
import { ImageRecognizerService } from '../services/image-recognizer.service';


@Component({
  selector: 'app-image-upload',
  templateUrl: './image-upload.component.html'
})
export class ImageUploadComponent{

  msg: string = ""
  image: any = null;

  get urlImagenDetecciones() { return this.imageRecognizerService.urlImagenDetecciones; }
  get isServiceWorking() { return this.imageRecognizerService.isworking; }

  constructor(private imageRecognizerService: ImageRecognizerService) { }

  selectImage(event: any) {
    this.image = null;
    this.imageRecognizerService.clearSteps(1);
    this.msg = "";

    if (!event.target.files[0] || event.target.files[0].length == 0) {
      this.msg = "Debes seleccionar una imagen";
      this.image = null;
      this.imageRecognizerService.clearSteps(1);
      return;
    }
    const mimeType = event.target.files[0].type;
    
    if(mimeType.match(/image\/*/) == null) {
      this.msg = "Debes seleccionar una imagen";
      this.image = null;
      this.imageRecognizerService.clearSteps(1);
      return;
    }

    const reader = new FileReader();
    reader.readAsDataURL(event.target.files[0]);

    reader.onload = (_event) => {
      this.msg = "";
      this.image = reader.result;
      this.image = new ImageUpload(event.target.files[0], reader.result);
    }
  }

  uploadImage() {
    this.imageRecognizerService.imageUpload(this.image.image);
  }
}

export class ImageUpload {
  constructor(public image: File, public url64: any) {}
}