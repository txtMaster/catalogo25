import type { IProducto } from "$lib/interfaces/IProducto";

export class Producto implements IProducto {
	constructor(codigo = "", nombre = "") {
		this.codigo = codigo;
		this.nombre = nombre;
	}
	public codigo: string = "";
	public nombre: string = "";
}
