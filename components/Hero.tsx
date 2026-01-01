import React from 'react';
import { ArrowRight, CheckCircle, Eye, MousePointerClick, BadgeDollarSign } from 'lucide-react';

const Hero: React.FC = () => {
  
  // Función para hacer scroll suave a las secciones
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <section className="relative pt-32 pb-20 overflow-hidden" id="hero">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="lg:grid lg:grid-cols-2 lg:gap-12 items-center">
          
          {/* COLUMNA IZQUIERDA: TEXTOS Y BOTONES */}
          <div>
            <h1 className="text-5xl lg:text-6xl font-extrabold text-slate-900 leading-[1.1] mb-6">
              Mentoría y Consultoría para Vendedores de <span className="text-[#041E42]">Mercado Libre</span>
            </h1>
            <p className="text-xl text-slate-600 mb-8 max-w-lg leading-relaxed">
              Acompañamos a vendedores de Mercado Libre a ordenar su cuenta, tomar mejores decisiones, y volver a crecer con criterio y método.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4 mb-10">
              
              {/* BOTÓN 1: AGENDAR (Enlace a Calendly) */}
              <a 
                href="https://calendly.com/fernandokosoy" 
                target="_blank" 
                rel="noopener noreferrer"
                className="bg-[#3CAA35] text-white px-8 py-4 rounded-xl font-bold flex items-center justify-center gap-2 hover:bg-[#2b7d26] transition-all shadow-lg shadow-green-200 cursor-pointer text-center"
              >
                Agendar llamada de diagnóstico
                <ArrowRight className="w-5 h-5" />
              </a>

              {/* BOTÓN 2: VER PROGRAMAS (Scroll suave a la sección 'programas') */}
              <button 
                onClick={() => scrollToSection('programas')}
                className="bg-white text-slate-700 border border-slate-200 px-8 py-4 rounded-xl font-bold hover:bg-slate-50 transition-all cursor-pointer"
              >
                Ver programas de mentoría
              </button>
            </div>

            {/* NUEVO: Badge Oficial de Consultora Certificada */}
            <div className="mt-8">
              <img 
                src="https://i.ibb.co/1YBLw3Vp/Captura-de-pantalla-2025-12-29-212348.png" 
                alt="Badge Consultora Certificada Mercado Libre" 
                // Ajusté la altura a h-20 para que se vea bien legible.
                // Si lo quieres más grande, prueba con h-24.
                className="h-20 w-auto object-contain"
              />
            </div>
          </div>

          {/* COLUMNA DERECHA: TARJETA "RADIOGRAFÍA" */}
          <div className="mt-12 lg:mt-0 relative">
            <div className="bg-white p-8 rounded-3xl shadow-2xl border border-slate-100 relative z-10">
              
              <div className="mb-8">
                <h3 className="text-2xl font-bold text-[#041E42]">Radiografía de tu cuenta</h3>
                <div className="h-1 w-20 bg-[#3CAA35] mt-2 rounded-full"></div>
              </div>

              <div className="space-y-6">
                
                {/* Ítem 1: Visibilidad / Posicionamiento */}
                <div className="flex gap-4 items-start">
                  <div className="w-12 h-12 bg-slate-50 rounded-xl flex items-center justify-center flex-shrink-0 border border-slate-100">
                    <Eye className="w-6 h-6 text-[#041E42]" />
                  </div>
                  <div>
                    <span className="block font-bold text-slate-900 text-lg">Visibilidad / Posicionamiento</span>
                    <span className="text-slate-600 leading-snug">Impresiones y clics de tus publicaciones.</span>
                  </div>
                </div>

                {/* Ítem 2: Conversión */}
                <div className="flex gap-4 items-start">
                  <div className="w-12 h-12 bg-slate-50 rounded-xl flex items-center justify-center flex-shrink-0 border border-slate-100">
                    <MousePointerClick className="w-6 h-6 text-[#041E42]" />
                  </div>
                  <div>
                    <span className="block font-bold text-slate-900 text-lg">Conversión</span>
                    <span className="text-slate-600 leading-snug">Ventas y tasa de conversión por tipo de producto.</span>
                  </div>
                </div>

                {/* Ítem 3: Rentabilidad */}
                <div className="flex gap-4 items-start">
                  <div className="w-12 h-12 bg-slate-50 rounded-xl flex items-center justify-center flex-shrink-0 border border-slate-100">
                    <BadgeDollarSign className="w-6 h-6 text-[#041E42]" />
                  </div>
                  <div>
                    <span className="block font-bold text-slate-900 text-lg">Rentabilidad</span>
                    <span className="text-slate-600 leading-snug">Inversión en anuncios, comisiones y margen real.</span>
                  </div>
                </div>

              </div>

              <div className="mt-8 pt-6 border-t border-slate-100">
                <p className="text-sm text-slate-500 italic flex gap-2">
                  <CheckCircle className="w-4 h-4 text-[#3CAA35] flex-shrink-0 mt-0.5" />
                  Estos son algunos de los indicadores que revisamos en el diagnóstico para entender qué frena tu crecimiento.
                </p>
              </div>
            </div>
            
            {/* Elementos de fondo decorativos */}
            <div className="absolute -top-10 -right-10 w-64 h-64 bg-[#3CAA35]/10 rounded-full blur-3xl -z-0"></div>
            <div className="absolute -bottom-10 -left-10 w-64 h-64 bg-[#041E42]/10 rounded-full blur-3xl -z-0"></div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;