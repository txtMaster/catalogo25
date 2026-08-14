import type { IClase } from "./IClase";
import type { IFamilia } from "./IFamilia";
import type { IProducto } from "./IProducto";
import type { ISegmento } from "./ISegmento";

export interface IArticulo {
	id: string;
	nombre: string;
	descripcion?: string;
}

export interface Clasificacion {
	articulo: IArticulo;
	segmento?: Seleccion<ISegmento>;
	familia?: Seleccion<IFamilia>;
	clase?: Seleccion<IClase>;
	producto?: Seleccion<IClase>;
}

export interface Seleccion<T> {
	eleccion?: T;
	motivo?: string;
	confianza?: number;
}
