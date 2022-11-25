import { Component } from '@angular/core';
import { ActionSheetController } from '@ionic/angular';
import { UserPhoto, PhotoService } from '../services/photo.service';
import { AngularFirestore } from '@angular/fire/compat/firestore';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss']
})
export class HomePage {
  dados: import("@angular/fire/compat/firestore").AngularFirestoreCollection<unknown>;

  constructor(
    public photoService: PhotoService,
    public firestore: AngularFirestore,
    public actionSheetController: ActionSheetController,
    private alertController: AlertController
    ) {}

  async ngOnInit() {
    await this.photoService.loadSaved();
  }

  async presentAlert() {
    const alert = await this.alertController.create({
      message: 'Cadastro no banco efetuado com sucesso!',
      buttons: ['OK'],
    });

    await alert.present();
  }

  public async showActionSheet(photo: UserPhoto, position: number) {
    const actionSheet = await this.actionSheetController.create({
      header: 'Photos',
      buttons: [{
        text: 'Delete',
        role: 'destructive',
        icon: 'trash',
        handler: () => {
          this.photoService.deletePicture(photo, position);
        }
      }, {
        text: 'Cancel',
        icon: 'close',
        role: 'cancel',
        handler: () => {
        
         }
      }]
    });
    await actionSheet.present();
  }

  enviarDados(){
    this.dados = this.firestore.collection('usuarios')
    this.dados.add({'nome': this.photoService.nome,'dataexpedicao': this.photoService.dataexpedicao,'cpf': this.photoService.cpf,'rg': this.photoService.rg})
    this.presentAlert()
  }
}
