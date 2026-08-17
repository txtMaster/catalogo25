import type { IClase } from "$lib/interfaces/IClase";
import type { Producto } from "./Producto";

export class Clase implements IClase {
	constructor(
		codigo: string = "",
		nombre: string = "",
		productos: Producto[] = [],
	) {
		this.codigo = codigo;
		this.nombre = nombre;
		this.productos = productos;
	}
	public codigo: string;
	public nombre: string = "";
	public productos: Producto[];
}
