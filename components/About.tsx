import React from 'react';
import { Linkedin, Check } from 'lucide-react';

const About: React.FC = () => {
  return (
    <section id="about" className="py-24 bg-white overflow-hidden">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="lg:grid lg:grid-cols-2 lg:gap-16 items-start">
          
          {/* COLUMNA FOTO */}
          <div className="relative mb-12 lg:mb-0">
            {/* Marco de la foto */}
            <div className="aspect-[4/5] bg-slate-100 rounded-[2.5rem] overflow-hidden shadow-2xl relative z-10">
              <img 
                src="https://i.ibb.co/N6WTNtcJ/fernando-kosoy.png" 
                alt="Fernando Kosoy" 
                className="w-full h-full object-cover"
              />
              
              {/* Etiqueta sobre la foto */}
              <div className="absolute bottom-8 left-8 text-white drop-shadow-md">
                <div className="bg-[#3CAA35] text-[10px] font-bold uppercase tracking-widest px-3 py-1 rounded-full w-fit mb-2 shadow-sm">
                  Founder & Senior Mentor
                </div>
                <h4 className="text-2xl font-bold drop-shadow-lg text-white">Fernando Kosoy</h4>
              </div>
            </div>

            {/* Elementos Decorativos de Fondo */}
            <div className="absolute -z-0 -top-6 -left-6 w-32 h-32 bg-[#3CAA35]/10 rounded-full"></div>
            <div className="absolute -z-0 -bottom-6 -right-6 w-48 h-48 border-2 border-slate-100 rounded-full"></div>
          </div>

          {/* COLUMNA TEXTO */}
          <div className="mt-4 lg:mt-0">
            <h2 className="text-4xl font-extrabold text-[#041E42] mb-6">Quién está detrás de Creseller</h2>
            
            <p className="text-lg text-slate-500 mb-8 leading-relaxed italic">
              Creseller es el espacio de consultoría y mentoría estratégica creado por <span className="text-[#041E42] font-semibold">Fernando Kosoy</span> para acompañar a vendedores de Mercado Libre en sus distintas etapas de crecimiento.
            </p>

            <div className="space-y-8 mb-10">
              <div>
                <h4 className="font-bold text-[#041E42] mb-2 text-xl">Fernando Kosoy</h4>
                <p className="text-xs text-[#3CAA35] uppercase tracking-widest font-bold mb-4">
                  CONSULTOR CERTIFICADO DE MERCADO LIBRE Y MENTOR ESTRATÉGICO
                </p>
                <p className="text-slate-600 leading-relaxed text-sm lg:text-base">
                  Vengo del mundo de las pymes y de la empresa familiar, por eso entiendo de cerca los desafíos de decidir qué hacer con cada peso, cada publicación y cada persona del equipo. Hoy acompaño a dueños y equipos a ordenar su cuenta de Mercado Libre y a tomar decisiones con datos, sin perder la esencia del negocio.
                </p>
              </div>

              <ul className="grid sm:grid-cols-2 gap-x-4 gap-y-6">
                {[
                  'Especialista en pymes y negocios familiares que venden en Mercado Libre.',
                  'Acompaño vendedores en sus lanzamientos hasta marcas consolidadas.',
                  'Foco en crecimiento con rentabilidad, no solo en facturación.',
                  'Trabajo 1 a 1 con dueños y equipos para ordenar operación.'
                ].map((text, idx) => (
                  <li key={idx} className="flex gap-3 text-sm text-slate-600 items-start">
                    <div className="mt-1 p-0.5 bg-[#3CAA35]/10 rounded flex-shrink-0">
                      <Check className="w-3.5 h-3.5 text-[#3CAA35]" />
                    </div>
                    <span>{text}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Cita Destacada */}
            <div className="p-6 bg-slate-50 rounded-2xl border-l-4 border-[#3CAA35] mb-8">
              <p className="text-lg font-medium text-[#041E42] italic">
                "Mi trabajo no es solo que vendas más, sino que entiendas por qué y cómo estás creciendo, para que puedas tomar mejores decisiones sobre tu negocio en Mercado Libre"
              </p>
            </div>

            {/* Link a LinkedIn (ACTUALIZADO) */}
            <a 
              href="https://www.linkedin.com/in/fernando-kosoy-800b052a/" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="inline-flex items-center gap-2 text-[#041E42] font-bold hover:text-[#3CAA35] transition-colors group"
            >
              <div className="p-2 bg-slate-100 rounded-full group-hover:bg-[#3CAA35]/10 transition-colors">
                <Linkedin className="w-5 h-5" />
              </div>
              Ver perfil en LinkedIn
            </a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;