import type { IProducto } from "./IProducto";

export interface IClase{
    codigo:string;
    nombre:string;
    productos:IProducto[];
}