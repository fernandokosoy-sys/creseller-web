
import React, { useState } from 'react';
import { ChevronDown, ChevronUp } from 'lucide-react';

const faqs = [
  {
    q: '¿En qué consiste el diagnóstico de cuenta de Mercado Libre?',
    a: 'Es una auditoría profunda de 360 grados donde analizamos tus métricas, catálogo, calidad de publicaciones, estrategia de precios, logística y gestión de reclamos para detectar fugas de dinero y oportunidades de crecimiento.'
  },
  {
    q: '¿Sirve la mentoría para vendedores nuevos?',
    a: 'Sí, contamos con el programa Despegue diseñado específicamente para quienes están empezando o tienen cuentas con poco movimiento y necesitan estructurar las bases correctamente para evitar errores costosos.'
  },
  {
    q: '¿Hacen optimización de publicaciones y anuncios?',
    a: 'Totalmente. Parte fundamental de nuestro método es la optimización técnica del catálogo (SEO para MELI) y el diseño de estrategias de Advertising (Product Ads) para maximizar el ROAS.'
  },
  {
    q: '¿Cuánto tiempo dura el acompañamiento?',
    a: 'Depende del programa elegido. El programa de Aceleración suele tener una duración inicial de 3 meses para lograr cambios estructurales y ver resultados tangibles.'
  }
];

const FAQ: React.FC = () => {
  const [openIdx, setOpenIdx] = useState<number | null>(0);

  return (
    <section className="py-24 bg-slate-50">
      <div className="max-w-4xl mx-auto px-4">
        <h2 className="text-3xl font-extrabold text-slate-900 text-center mb-12">Preguntas Frecuentes sobre Consultoría Mercado Libre</h2>
        
        <div className="space-y-4">
          {faqs.map((faq, idx) => (
            <div key={idx} className="bg-white rounded-2xl border border-slate-200 overflow-hidden transition-all shadow-sm">
              <button 
                onClick={() => setOpenIdx(openIdx === idx ? null : idx)}
                className="w-full flex items-center justify-between p-6 text-left hover:bg-slate-50 transition-colors"
              >
                <span className="font-bold text-slate-800">{faq.q}</span>
                {openIdx === idx ? <ChevronUp className="text-primary-green" /> : <ChevronDown className="text-slate-400" />}
              </button>
              {openIdx === idx && (
                <div className="p-6 pt-0 text-slate-600 leading-relaxed border-t border-slate-50 animate-fadeIn">
                  {faq.a}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FAQ;
