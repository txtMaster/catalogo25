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
	segmento: Seleccion<ISegmento | null>;
	familia: Seleccion<IFamilia | null>;
	clase: Seleccion<IClase | null>;
	producto: Seleccion<IProducto | null>;
};

export interface Seleccion<T> {
	eleccion?: T;
	motivo?: string;
	confianza?: number;
}
export function limpiarSeleccion(s: Seleccion<any>) {
	s.confianza = undefined;
	s.motivo = undefined;
	s.eleccion = undefined;
}

export const clasificacionToArray = {
	keys: [
		"id",
		"nombre",
		"descripcion",
		"segmento",
		"familia",
		"clase",
		"producto",
	],
	exec(cls: Clasificacion) {
		return [
			cls.articulo.id,
			cls.articulo.nombre,
			cls.articulo.descripcion,
			cls.segmento.eleccion?.codigo,
			cls.familia.eleccion?.codigo,
			cls.clase.eleccion?.codigo,
			cls.producto.eleccion?.codigo,
		];
	},
};
