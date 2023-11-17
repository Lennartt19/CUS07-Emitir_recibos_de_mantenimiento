import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Casas } from 'src/app/models/casas';

@Component({
  selector: 'app-registrar-gasto-casa',
  templateUrl: './registrar-gasto-casa.component.html',
  styleUrls: ['./registrar-gasto-casa.component.css']
})
export class RegistrarGastoCasaComponent implements OnInit {
  @Output() mostrarRegistroCasa_OUT = new EventEmitter<boolean>();
  @Output() idCasaRegistro_OUT = new EventEmitter<string>();
  @Input() casasArray_IN: Casas[] = [];

  // DATOS DE LA CASA
  num_casa_selected: string = '--N° Casa--';
  id_casa_selected: string = '';

  montoEditable: number | null = null;
  montoSeleccionado: number | null = null; // Nueva propiedad para almacenar el monto seleccionado

  listaTipoGastoCasas: any[] = ['Gasto generico', 'Sanciones'];
  listaDescripcionCasas: any[] = ['Agua', 'Luz y Electricidad'];

  gatosRegistradosCasa: any[] = [
    { TipoGasto: 'Gasto de agua individual', Monto: 30 },
    { TipoGasto: 'Administración y contabilidad ', Monto: 66 },
    { TipoGasto: 'Teléfono fijo e internet', Monto: 12.3 },
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605', Monto: 12.3 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613', Monto: 12.3 },
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 30.5 },
    { TipoGasto: 'Administración y contabilidad ', Monto: 66.0 },
    { TipoGasto: 'Teléfono fijo e internet', Monto: 12.3 },
    { TipoGasto: 'Maltratar-faltar el respeto al personal', Monto: 12.3 },
    { TipoGasto: 'Utilizar el estacionamiento como depocito', Monto: 12.3 }
  ];

  gatosRegistradosPredio: any[] = [
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305 },
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613', Monto: 123 },
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305 },
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613', Monto: 123 },
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305 },
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613', Monto: 123 },
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305 },
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605', Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613', Monto: 123 }
  ];

  ngOnInit() {
    // Recuperar datos almacenados localmente al cargar el componente
    const storedData = localStorage.getItem('gastosRegistradosCasa');
    if (storedData) {
      this.gatosRegistradosCasa = JSON.parse(storedData);
    }
  }

  set_mostrarRegistroCasa(item: boolean) {
    this.mostrarRegistroCasa_OUT.emit(item);
  }

  registrarGasto() {
    // Obtén el monto correspondiente al tipo de gasto seleccionado
    const tipoGastoSeleccionado = 'Gasto de agua individual'; // Cambia esto según tu lógica
    const gastoEncontrado = this.gatosRegistradosCasa.find(gasto => gasto.TipoGasto === tipoGastoSeleccionado);

    // Asigna el monto encontrado a la propiedad montoSeleccionado
    this.montoSeleccionado = gastoEncontrado ? gastoEncontrado.Monto : null;
  }

  finalizarRegistroCasa() {
    // Aca iría el método para modificar la tabla ESTADO_REGISTRO_PREDIO de la BD
    localStorage.setItem('gastosRegistradosCasa', JSON.stringify(this.gatosRegistradosCasa));
    alert('Se han actualizado correctamente los gastos');
    window.location.reload();
  }

  editarMonto(gasto: any) {
    if (this.montoEditable === null) {
      // Si no se está editando ningún monto, permite la edición para este gasto
      this.montoEditable = gasto.Monto;
      this.montoSeleccionado = gasto.Monto; // Agregamos esta línea para almacenar el monto original
    } else {
      // Si se está editando algún monto, guarda los cambios y limpia la variable editable
      gasto.Monto = this.montoEditable;
      this.montoEditable = null;
      this.montoSeleccionado = null; // Limpiamos la variable montoSeleccionado
    }
  }
}
