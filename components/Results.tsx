
import React from 'react';
import { Quote, Star } from 'lucide-react';

const testimonials = [
  {
    rubro: 'HERRAMIENTAS',
    situation: 'Ventas estancadas y falta de planificación de pautas publicitarias.',
    result: 'En 3 meses ordenamos el catálogo y la inversión. Pasamos de un crecimiento plano a un aumento sostenido, manteniendo un ACOS saludable.',
    author: 'Juan Pablo',
    role: 'MercadoLíder Platinum'
  },
  {
    rubro: 'DECORACIÓN',
    situation: 'Gran volumen, muchos reclamos y operación en riesgo.',
    result: 'Ordenamos el depósito y la atención. Recuperamos el termómetro verde y ahora somos Tienda Oficial.',
    author: 'María',
    role: 'Dueña de Pyme'
  },
  {
    rubro: 'AUTOPARTES',
    situation: 'Nueva unidad de negocio que no arrancaba por falta de experiencia.',
    result: 'El diagnóstico reveló errores en títulos y fichas. Con ese ajuste logramos el Top 3 de la categoría con mejor rentabilidad.',
    author: 'Lucas',
    role: 'Gerente Comercial'
  }
];

const Results: React.FC = () => {
  return (
    <section className="py-24 bg-white">
      <div className="max-w-7xl mx-auto px-4 text-center mb-16">
        <h2 className="text-4xl font-extrabold text-slate-900 mb-6">Resultados que hablan</h2>
        <p className="text-slate-500 max-w-2xl mx-auto text-lg">
          Algunos de los resultados que consiguieron los vendedores que ordenaron su cuenta con Creseller.
        </p>
      </div>

      <div className="max-w-7xl mx-auto px-4 grid lg:grid-cols-3 gap-8">
        {testimonials.map((t, i) => (
          <div key={i} className="bg-soft-gray p-8 rounded-3xl border border-slate-100 relative group transition-all duration-300 hover:shadow-xl hover:bg-white">
            <Quote className="absolute top-6 right-8 w-12 h-12 text-slate-200 group-hover:text-primary-green/20" />
            
            <div className="mb-8">
              <span className="inline-block px-3 py-1 bg-blue-100 text-blue-700 text-[10px] font-bold uppercase tracking-widest rounded-md mb-4">
                Rubro: {t.rubro}
              </span>
              <div className="mb-4">
                <h4 className="text-xs font-bold text-slate-400 uppercase tracking-widest mb-2">Situación inicial:</h4>
                <p className="text-slate-600 text-sm leading-relaxed">{t.situation}</p>
              </div>
              <div>
                <h4 className="text-xs font-bold text-primary-green uppercase tracking-widest mb-2">Resultado:</h4>
                <p className="text-slate-900 font-semibold leading-relaxed">"{t.result}"</p>
              </div>
            </div>

            <div className="flex items-center gap-3 pt-6 border-t border-slate-200">
              <div className="w-10 h-10 rounded-full bg-slate-200 flex items-center justify-center font-bold text-slate-500">
                {t.author[0]}
              </div>
              <div>
                <p className="text-sm font-bold text-slate-900">{t.author}</p>
                <p className="text-xs text-slate-500">{t.role}</p>
              </div>
              <div className="ml-auto flex">
                {[...Array(5)].map((_, idx) => (
                  <Star key={idx} className="w-3 h-3 text-yellow-400 fill-current" />
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Results;
