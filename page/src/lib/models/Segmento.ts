import type { ISegmento } from "$lib/interfaces/ISegmento";
import type { Familia } from "./Familia";

export class Segmento implements ISegmento {
	constructor(codigo: string = "", nombre: string = "", familias: Familia[]) {
		this.codigo = codigo;
		this.nombre = nombre;
		this.familias = familias;
	}
	public codigo: string = "";
	public nombre: string = "";
	public familias: Familia[];
}
