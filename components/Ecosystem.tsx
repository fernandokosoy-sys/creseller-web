
import React from 'react';
import { ShoppingBag, Laptop, BarChart2 } from 'lucide-react';

const Ecosystem: React.FC = () => {
  return (
    <section className="py-24 bg-soft-gray border-y border-slate-100">
      <div className="max-w-7xl mx-auto px-4 text-center mb-16">
        <h2 className="text-3xl font-extrabold text-slate-900 mb-4">Creseller dentro de un ecosistema real de venta en Mercado Libre</h2>
        <p className="text-slate-500 max-w-2xl mx-auto">
          Creseller no nace en un Excel ni en una presentación, sino dentro de un ecosistema real de venta en Mercado Libre. Opero y acompaño diferentes unidades de negocio que venden todos los días, y desde esa experiencia conecto consultoría, marcas y operación para potenciar cada cuenta.
        </p>
      </div>

      <div className="max-w-7xl mx-auto px-4 grid md:grid-cols-3 gap-8">
        <div className="bg-white p-8 rounded-3xl shadow-sm border border-slate-100">
          <div className="w-12 h-12 bg-blue-50 text-blue-600 rounded-2xl flex items-center justify-center mb-6">
            <ShoppingBag className="w-6 h-6" />
          </div>
          <h4 className="text-lg font-bold text-slate-900 mb-3">Operación y marcas</h4>
          <p className="text-slate-500 text-sm leading-relaxed">
            Gestión de cuentas que venden productos en Mercado Libre: hogar, organización, textiles y más. Lo que enseñamos en la consultoría se prueba y ajusta en operación real.
          </p>
        </div>

        <div className="bg-slate-900 text-white p-8 rounded-3xl shadow-xl transform md:-translate-y-4">
          <div className="w-12 h-12 bg-primary-green text-slate-900 rounded-2xl flex items-center justify-center mb-6">
            <Laptop className="w-6 h-6" />
          </div>
          <h4 className="text-lg font-bold mb-3">Consultoría y mentoría — Creseller</h4>
          <p className="text-slate-300 text-sm leading-relaxed">
            Acompañamiento 1 a 1 para dueños y equipos. Traducimos todo ese saber real en el día a día para que tu cuenta dé saltos de rentabilidad y organización.
          </p>
        </div>

        <div className="bg-white p-8 rounded-3xl shadow-sm border border-slate-100">
          <div className="w-12 h-12 bg-green-50 text-green-600 rounded-2xl flex items-center justify-center mb-6">
            <BarChart2 className="w-6 h-6" />
          </div>
          <h4 className="text-lg font-bold text-slate-900 mb-3">Desarrollo comercial del seller</h4>
          <p className="text-slate-500 text-sm leading-relaxed">
            El objetivo no es solo optimizar publicaciones, sino desarrollar carrera comercial del vendedor: criterio, método, números y visión de negocio para crecer más allá de una sola cuenta.
          </p>
        </div>
      </div>

      <div className="mt-16 max-w-3xl mx-auto text-center px-4">
        <div className="bg-blue-50 border border-blue-100 rounded-2xl p-6">
          <p className="text-blue-800 font-medium italic">
            "No estás solo en Mercado Libre: te sumas a un ecosistema de operación, marcas y consultoría que trabaja todos los días dentro del marketplace."
          </p>
        </div>
      </div>
    </section>
  );
};

export default Ecosystem;
