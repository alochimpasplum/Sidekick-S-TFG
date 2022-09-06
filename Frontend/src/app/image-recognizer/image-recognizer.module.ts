import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageUploadComponent } from './image-upload/image-upload.component';
import { RecognizerComponent } from './recognizer/recognizer.component';
import { MermaidModule } from '../mermaid/mermaid.module';
import { AskCodeComponent } from './ask-code/ask-code.component';
import { CodeViewerComponent } from './code-viewer/code-viewer.component';
import { LanguageComponent } from './code-viewer/language/language.component';



@NgModule({
  declarations: [
    ImageUploadComponent,
    RecognizerComponent,
    AskCodeComponent,
    CodeViewerComponent,
    LanguageComponent
  ],
  exports: [
    RecognizerComponent
  ],
  imports: [
    CommonModule,
    MermaidModule
  ]
})
export class ImageRecognizerModule { }
