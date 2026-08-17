import type { IClase } from "./IClase";
import type { IFamilia } from "./IFamilia";
import type { IProducto } from "./IProducto";
import type { ISegmento } from "./ISegmento";

export interface IArticulo {
	id: string;
	nombre: string;
	descripcion?: string;
}

export type Clasificacion = {
	articulo: IArticulo;
	segmento: Seleccion<ISegmento|null>;
	familia: Seleccion<IFamilia|null>;
	clase: Seleccion<IClase|null>;
	producto: Seleccion<IProducto|null>;
}

export interface Seleccion<T> {
	eleccion?: T;
	motivo?: string;
	confianza?: number;
}
