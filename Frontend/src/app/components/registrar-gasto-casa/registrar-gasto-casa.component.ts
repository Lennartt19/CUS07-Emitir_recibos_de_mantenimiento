import { Component, OnInit, EventEmitter, Input,Output } from '@angular/core';
import { Casas } from 'src/app/models/casas';
import { ConexionService } from 'src/app/services/conexion.service';
import { PredioGastosDet } from 'src/app/models/predio-gastos-det';
import { TipoGastos } from 'src/app/models/tipo-gastos';
import { DescripGastos } from 'src/app/models/descrip-gastos';

@Component({
  selector: 'app-registrar-gasto-casa',
  templateUrl: './registrar-gasto-casa.component.html',
  styleUrls: ['./registrar-gasto-casa.component.css']
})
export class RegistrarGastoCasaComponent{

  constructor(private connBackend: ConexionService) { }

  id_predio: string =         '';
  id_periodo: string =        '';
  id_gasto: string =          '';
  periodo: string =           '';
  nombrePredio: string =      '';
  montoTotal: number =        0;
  botonUR =                   'Registrar';
  id_gasto_especifico: string = '';

  @Output() mostrarRegistroCasa_OUT = new EventEmitter<boolean>();
  @Output() idCasaRegistro_OUT = new EventEmitter<string>();
  @Input() casasArray_IN: Casas[] = [];

  //Agregados para conección con bd
  @Output() mostrarRegistroPredio_OUT = new EventEmitter<boolean>();
  @Input() id_predio_IN:    string = "";
  @Input() id_periodo_IN:   string = "";
  @Input() predio_IN:       string = "";
  @Input() periodo_IN:      string = "";
  
  // DATOS DE LA CASA
  num_casa_selected: string = '--N° Casa--';
  id_casa_selected: string = '';

  montoEditable: number | null = null;
  montoSeleccionado: number | null = null; // Nueva propiedad para almacenar el monto seleccionado

  listaTipoGastoCasas: any[] = ['Gasto generico', 'Sanciones'];
  listaDescripcionCasas: any[] = ['Agua', 'Luz y Electricidad'];
  
  
  gatosRegistradosCasa: any[] = [
    { TipoGasto: 'Gasto de agua individual', Monto: 30},
    { TipoGasto: 'Administración y contabilidad ', Monto: 66 },
    { TipoGasto: 'Teléfono fijo e internet',  Monto: 12.3},
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605',  Monto: 12.3 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613',  Monto: 12.3},
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 30.5},
    { TipoGasto: 'Administración y contabilidad ', Monto: 66.0 },
    { TipoGasto: 'Teléfono fijo e internet',  Monto: 12.3},
    { TipoGasto: 'Maltratar-faltar el respeto al personal',  Monto: 12.3},
    { TipoGasto: 'Utilizar el estacionamiento como depocito',  Monto: 12.3}
  ];

  /*
  gatosRegistradosPredio: any[] = [
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305},
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet',  Monto: 123},
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605',  Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613',  Monto: 123},
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305},
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet',  Monto: 123},
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605',  Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613',  Monto: 123},
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305},
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet',  Monto: 123},
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605',  Monto: 123 },
    { TipoGasto: 'Planilla (portería- áreas comunes- limpieza)', Monto: 305},
    { TipoGasto: 'Administración y contabilidad ', Monto: 660 },
    { TipoGasto: 'Teléfono fijo e internet',  Monto: 123},
    { TipoGasto: 'Consumo de Luz Mensual SS-GG -Suministro 1695605',  Monto: 123 },
    { TipoGasto: 'Consumo de Luz Mensual BCI -Suministro 1695613',  Monto: 123}
  ];*/

  /*
  ngOnInit() {
    // Recuperar datos almacenados localmente al cargar el componente
    
    
    const storedData = localStorage.getItem('gastosRegistradosCasa');
    if (storedData) {
      this.gatosRegistradosCasa = JSON.parse(storedData);
    }
  }*/

  gastosRegistradosArray: PredioGastosDet[] = [];

  ngOnInit() {
    this.nombrePredio = this.predio_IN;
    this.periodo = this.periodo_IN;
    this.id_predio = this.id_predio_IN;
    this.id_periodo = this.id_periodo_IN;
    this.getGastosDet_BD();
  }

  //MUESTRA Y FINALIZACIÓN DE ASIGNAR GASTOS AL PREDIO
  set_mostrarRegistroPredio(item: boolean) {
    this.mostrarRegistroPredio_OUT.emit(item);
  }

  set_mostrarRegistroCasa(item: boolean) {
    this.mostrarRegistroCasa_OUT.emit(item);
  }

  /*
  gastoRegistrado() {
    const gastoRegistrado01 = this.gastosRegistradosArray.filter((gasto) => gasto.id_gasto === this.id_gasto);
    if(gastoRegistrado01.length > 0){
      return true;
    }
    else{
      return false;
    }
  }*/

  registrarGasto() {
    // Verifica que se haya seleccionado una descripción y un número de casa
    if (this.num_casa_selected === '--N° Casa--' || !this.listaDescripcionCasas || this.listaDescripcionCasas.length === 0) {
      alert('Por favor, seleccione una descripción antes de registrar el gasto.');
      return;
    }
  
    // Obtén el monto correspondiente al tipo de gasto seleccionado
    let tipoGastoSeleccionado: string;
  
    if (this.listaDescripcionCasas.includes('Agua')) {
      tipoGastoSeleccionado = 'Gasto de agua individual';
    } else if (this.listaDescripcionCasas.includes('Luz y Electricidad')) {
      tipoGastoSeleccionado = 'Consumo de Luz Mensual SS-GG -Suministro 1695605';
    } else {
      // Manejo de caso por defecto si no coincide con ninguna descripción conocida
      console.error('Descripción no reconocida:', this.listaDescripcionCasas);
      return;
    }
    
    
    const gastoEncontrado = this.gatosRegistradosCasa.find(gasto => gasto.TipoGasto === tipoGastoSeleccionado);
  
    // Asigna el monto encontrado a la propiedad montoSeleccionado
    this.montoSeleccionado = gastoEncontrado ? gastoEncontrado.Monto : null;
  }

  //vamos a crear una función que me permita catpurar el id_periodo seleccionado
  

  getGastosDet_BD(): void {
    this.connBackend.getGastosPredios(this.id_periodo='581')
      .subscribe(data => {
        console.log(data)
        this.gastosRegistradosArray = data.gastoPredioDetalle;
      },
        error => console.log(error));
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
