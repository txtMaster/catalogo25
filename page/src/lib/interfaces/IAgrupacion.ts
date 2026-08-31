import type { Clasificacion } from "./IArticulo";

export type IAgrupacion = {
	sinDescripcion: Set<Clasificacion>;
	segmentos: Set<Clasificacion>;
	familias: Set<Clasificacion>;
	clases: Set<Clasificacion>;
	productos: Set<Clasificacion>;
	vacios: Set<Clasificacion>;
};
