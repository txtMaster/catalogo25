const API_URL = import.meta.env.VITE_API_URL;
const API_KEY = import.meta.env.VITE_API_KEY;

export type context = {
	pais: string;
	rubro: string;
};

export const API = {
	descripcion: {
		async generate(context: context, payload: Array<[string, string]>): Promise<Response> {
			return fetch(API_URL + "/descripcion/generar", {
				method: "POST",
                headers:{
                    "Content-Type":"application/json"
                },
				body: JSON.stringify({
					clave: API_KEY,
                    contexto:context,
					articulos: payload,
				}),
			});
		},
	},
};
