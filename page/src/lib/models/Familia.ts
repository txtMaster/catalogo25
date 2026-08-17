import type { IFamilia } from "$lib/interfaces/IFamilia";
import type { Clase } from "./Clase";

export class Familia implements IFamilia {
	constructor(codigo = "", nombre: string = "", clases: Clase[] = []) {
		this.codigo = codigo;
		this.nombre = nombre;
		this.clases = clases;
	}
	public codigo: string;
	public nombre: string;
	public clases: Clase[];
}
