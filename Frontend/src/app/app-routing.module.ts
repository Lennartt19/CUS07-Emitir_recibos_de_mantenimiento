import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { RecaudacionComponent } from './components/recaudacion/recaudacion.component';
import { SeguimientoComponent } from './components/seguimiento/seguimiento.component';
import { CotizacionComponent } from './components/cotizacion/cotizacion.component';
import { MantenimientoRecibosComponent } from './components/mantenimiento-recibos/mantenimiento-recibos.component';
const routes: Routes = [
  {
    path:'RegistrarRecaudacion', component:RecaudacionComponent,
  },
  {
    path: 'SeguimientoCotizacion', component:SeguimientoComponent,
  },
  {
    path: 'SeguimientoCotizacion/cotizacion/:id_solicitud', component:CotizacionComponent,
  },
  {
    path: 'EmitirRecibos', component:MantenimientoRecibosComponent,
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
