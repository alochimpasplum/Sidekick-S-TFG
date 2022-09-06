import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { GetMermaidFromImage } from 'src/app/interfaces/getMermaidFromImage.interface';
import { MermaidBlock } from 'src/app/interfaces/getMermaidFromImage.interface';
import { Codes, Language } from '../../interfaces/Codes';
import { Buffer } from 'buffer/';

@Injectable({
  providedIn: 'root'
})
export class ImageRecognizerService {

  private _backendUrl: string = 'http://127.0.0.1:5000';
  private _urlImagenDetecciones: string = "";
  private _urlImagenMermaid: string = "";
  private _mermaidBlocks: MermaidBlock[] = [];
  private _serverLanguajes: string[] = [];
  private _isWorking: boolean = false;
  private _mermaidReady: boolean = false;
  private _isMermaidBlocksChanges: boolean = false;
  private _languages: Language[] = [];

  get urlImagenDetecciones() {return this._urlImagenDetecciones;}
  set urlImagenDetecciones(value: string) { this._urlImagenDetecciones = value; }

  get mermaidBlocks() { return this._mermaidBlocks; }
  get urlImagenMermaid() { return this._urlImagenMermaid; }
  get mermaidReady() { return this._mermaidReady; }
  get isworking() { return this._isWorking; }
  get isMermaidBlocksChanges() { return this._isMermaidBlocksChanges; }
  get serverLanguajes() { return this._serverLanguajes; }
  get languages() { return this._languages; }

  constructor(private http: HttpClient) {
    this.getSupportedLanguages();
  }

  getSupportedLanguages(): void {
    this.http.get<any>(`${this._backendUrl}/getSupportedLanguages`)
    .subscribe( (resp) => {
      console.log(resp);
      this._serverLanguajes = resp.SupportedLanguages;
    });
  }

  clearSteps(step: number) : void {
    switch (step) {
      // todo: probar esto:
      // @ts-ignore
      case 1:
        this._urlImagenDetecciones = "";
      case 2:
        this._mermaidReady = false;
        this._isMermaidBlocksChanges = false;
        this._urlImagenMermaid = "";
        this._isWorking = false;
        this._mermaidBlocks = [];
        break;
    }
  }

  imageUpload(image: File) : void {
    this.clearSteps(1);
    this.getSupportedLanguages();

    this._urlImagenDetecciones = 'assets/img/loading.gif';
    const formData: FormData = new FormData();
    formData.append('image', image, image.name);
    
    this._isWorking = true;
    this._mermaidReady = false;
    this.http.post<GetMermaidFromImage>(`${this._backendUrl}/getMermaidFromImage`, formData)
      .subscribe( (resp) => {
        console.log(resp);
        if (resp.image_with_detections == ""){
          // todo: incluir una imagen o algo que diga que no se ha cargado
          this._urlImagenDetecciones = "";
        } else {
          this._urlImagenDetecciones = resp.image_with_detections;
        }
        if(resp.image_mermaid != "" || resp.mermaid_blocks != null){
          if (resp.image_mermaid == ""){
            // todo: incluir una imagen o algo que diga que no se ha cargado
            this._urlImagenMermaid = "";
          } else {
            this._urlImagenMermaid = resp.image_mermaid;
          }
          if (resp.mermaid_blocks == null){
            // todo: que hace el programa en caso de que exista algún fallo
          } else {
            this._mermaidBlocks = resp.mermaid_blocks;
          }
          this._mermaidReady = true;
        }
        
        this._isWorking = false;
      });
  }

  modifyMermaidBlocks(block: MermaidBlock): void {
    this._isMermaidBlocksChanges = true;
    let blockToRemove: MermaidBlock = this._mermaidBlocks.find(element => element.block_name == block.block_name)!;
    let index = this._mermaidBlocks.indexOf(blockToRemove);
    this._mermaidBlocks.splice(index, 1, block);
  }

  modifyMermaidDiagram(): void {
    this._isWorking = true;

    let params: HttpParams = new HttpParams().set("MermaidBlocks", JSON.stringify(this._mermaidBlocks));

    this.http.get<any>(`${this._backendUrl}/getMermaidImage`, {params})
      .subscribe( (resp) => {
        console.log(resp);
        if(resp != ""){
          this._urlImagenMermaid = resp.image_mermaid;
        }
        this._isWorking = false;
        this._isMermaidBlocksChanges = false;
      });
  }

  getCode(languages: string[]): void {
    this._isWorking = true;
    var codes: Language[] = []

    let params: HttpParams = new HttpParams().set("Languages", JSON.stringify(languages)).set("MermaidBlocks", JSON.stringify(this._mermaidBlocks));
    console.log(params);
    this.http.get<Codes>(`${this._backendUrl}/getCode`, {params})
      .subscribe( (resp) => {
        for (let [key, value] of Object.entries(resp)){
          let lang: Language = {
            language_name: key,
            code: Buffer.from(value, 'base64').toString()
          };
          codes.push(lang);
        }
        this._languages = codes;
        console.log(this._languages);
        
        this._isWorking = false;
      });
  }
}