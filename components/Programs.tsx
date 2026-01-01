
import React from 'react';
import { Check, Calendar, ArrowRight } from 'lucide-react';

const Programs: React.FC = () => {
  return (
    <section id="programas" className="py-24 bg-slate-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* ENCABEZADO */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <h2 className="text-4xl font-extrabold text-[#041E42] mb-6">
            Programas de mentoría y consultoría
          </h2>
          <p className="text-xl text-slate-600 leading-relaxed">
            Diseñamos cada programa según el momento real de tu cuenta: <span className="font-bold text-[#041E42]">creer</span> para iniciar con bases firmes, <span className="font-bold text-[#041E42]">crear</span> para ordenar y optimizar, y <span className="font-bold text-[#041E42]">crecer</span> para escalar con visión estratégica.
          </p>
        </div>

        {/* GRILLA DE PROGRAMAS */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-start">
          
          {/* TARJETA 1: DESPEGUE (Light) */}
          <div className="bg-white rounded-3xl p-8 border border-slate-200 shadow-lg flex flex-col h-full hover:shadow-xl transition-shadow duration-300">
            <div className="mb-6">
              <h3 className="text-3xl font-bold text-[#041E42] mb-2">Despegue</h3>
              <p className="text-sm font-bold text-slate-400 tracking-widest uppercase">Para arrancar con fuerza</p>
            </div>
            <p className="text-slate-600 mb-8 leading-relaxed text-sm">
              Ideal para ordenar tu cuenta, entender la lógica del algoritmo y dejar de "probar" para salir al público.
            </p>
            <ul className="space-y-4 mb-8 flex-1">
              {[
                'Diagnóstico completo de cuenta y categorías de productos.',
                'Revisión y mejora de títulos, fotos y descripciones de tus publicaciones clave.',
                'Comprensión práctica del algoritmo.',
                'Plan de acción para los próximos 30–60 días.'
              ].map((item, idx) => (
                <li key={idx} className="flex gap-3 text-sm text-slate-700">
                  <Check className="w-5 h-5 text-[#3CAA35] flex-shrink-0" />
                  {item}
                </li>
              ))}
            </ul>
            <a href="https://calendly.com/fernandokosoy" target="_blank" rel="noopener noreferrer" className="w-full block text-center py-3 rounded-xl border-2 border-slate-100 text-[#041E42] font-bold hover:border-[#041E42] hover:bg-slate-50 transition-all">
              Consultar programa
            </a>
          </div>

          {/* TARJETA 2: ACELERACIÓN (Dark / Highlighted) */}
          <div className="bg-[#041E42] rounded-3xl p-8 border border-[#041E42] shadow-2xl flex flex-col h-full relative transform lg:-translate-y-4 lg:scale-105 z-10">
            {/* Badge "Más Elegido" */}
            <div className="absolute top-0 right-8 transform -translate-y-1/2 bg-[#3CAA35] text-white text-xs font-bold px-4 py-1.5 rounded-full shadow-lg border-2 border-[#041E42]">
              ⚡ MÁS ELEGIDO
            </div>

            <div className="mb-6 mt-2">
              <h3 className="text-3xl font-bold text-white mb-2">Aceleración</h3>
              <p className="text-sm font-bold text-[#3CAA35] tracking-widest uppercase">Para ordenar y escalar</p>
            </div>
            <p className="text-slate-300 mb-8 leading-relaxed text-sm">
              Acompañamiento uno-a-uno para vendedores que ya venden, pero sienten desorden, estancamiento o baja rentabilidad.
            </p>
            <ul className="space-y-4 mb-10 flex-1">
              {[
                'Método de trabajo aplicable semana a semana.',
                'Gestión comercial eficiente: stock, precios y márgenes.',
                'Estrategia de anuncios y optimización de inversión.',
                'Planificación detallada para alcanzar metas.'
              ].map((item, idx) => (
                <li key={idx} className="flex gap-3 text-sm text-slate-200">
                  <Check className="w-5 h-5 text-[#3CAA35] flex-shrink-0" />
                  {item}
                </li>
              ))}
            </ul>
            <a 
              href="https://calendly.com/fernandokosoy" 
              target="_blank" 
              rel="noopener noreferrer"
              className="w-full flex items-center justify-center gap-2 py-4 rounded-xl bg-[#3CAA35] text-white font-bold hover:bg-[#2b7d26] transition-all shadow-lg shadow-green-900/20"
            >
              <Calendar className="w-4 h-4" />
              Agendar diagnóstico
            </a>
          </div>

          {/* TARJETA 3: CONSOLIDACIÓN (Light) */}
          <div className="bg-white rounded-3xl p-8 border border-slate-200 shadow-lg flex flex-col h-full hover:shadow-xl transition-shadow duration-300">
            <div className="mb-6">
              <h3 className="text-3xl font-bold text-[#041E42] mb-2">Consolidación</h3>
              <p className="text-sm font-bold text-slate-400 tracking-widest uppercase">Para líderes de categoría</p>
            </div>
            <p className="text-slate-600 mb-8 leading-relaxed text-sm">
              Mentoría estratégica 1 a 1 para dueños de negocios y equipos que necesitan claridad directiva y foco en el largo plazo.
            </p>
            <ul className="space-y-4 mb-8 flex-1">
              {[
                'Visión de negocio a largo plazo para crecimiento sostenible.',
                'Toma de decisiones de inversión y estructura.',
                'Plan de escalado y expansión a nuevas categorías.'
              ].map((item, idx) => (
                <li key={idx} className="flex gap-3 text-sm text-slate-700">
                  <Check className="w-5 h-5 text-[#3CAA35] flex-shrink-0" />
                  {item}
                </li>
              ))}
            </ul>
            <a href="https://calendly.com/fernandokosoy" target="_blank" rel="noopener noreferrer" className="w-full block text-center py-3 rounded-xl border-2 border-slate-100 text-[#041E42] font-bold hover:border-[#041E42] hover:bg-slate-50 transition-all">
              Consultar programa
            </a>
          </div>

        </div>

        {/* EXTRA CTA */}
        <div className="mt-16 text-center">
          <a href="https://calendly.com/fernandokosoy" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-[#041E42] font-semibold hover:text-[#3CAA35] transition-colors">
            ¿No sabés qué programa es para vos? Quiero saber cuál es para mí
            <ArrowRight className="w-4 h-4" />
          </a>
        </div>

      </div>
    </section>
  );
};

export default Programs;