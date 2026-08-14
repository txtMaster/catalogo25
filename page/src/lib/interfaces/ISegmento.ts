import type { IFamilia } from "./IFamilia";

export interface ISegmento{
    codigo:string;
    nombre:string;
    familias:IFamilia[];
}