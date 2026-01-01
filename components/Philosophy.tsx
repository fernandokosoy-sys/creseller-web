import React from 'react';
import { Quote } from 'lucide-react';

const Philosophy: React.FC = () => {
  return (
    <section className="bg-slate-50 py-20 px-4 sm:px-6 lg:px-8">
      <div className="max-w-6xl mx-auto">
        
        {/* TARJETA CONTENEDORA */}
        <div className="bg-white rounded-3xl shadow-xl overflow-hidden border border-slate-100">
          <div className="grid lg:grid-cols-5">
            
            {/* COLUMNA IZQUIERDA: EL PROBLEMA (Fondo Azul Oscuro) */}
            <div className="bg-[#041E42] p-10 lg:p-12 lg:col-span-2 flex flex-col justify-center relative overflow-hidden">
              {/* Decoración de fondo */}
              <div className="absolute top-0 left-0 w-32 h-32 bg-[#3CAA35]/10 rounded-full blur-3xl"></div>
              
              <Quote className="w-10 h-10 text-[#3CAA35] mb-6 opacity-80" />
              
              <p className="text-white/90 text-lg md:text-xl font-medium leading-relaxed italic">
                "Entendemos los momentos de duda, estancamiento y confusión cuando la cuenta deja de crecer."
              </p>
            </div>

            {/* COLUMNA DERECHA: LA SOLUCIÓN (Fondo Blanco) */}
            <div className="p-10 lg:p-12 lg:col-span-3 flex flex-col justify-center bg-white">
              <div className="space-y-8">
                
                {/* Ítem 1: CREER */}
                <div className="flex gap-4 items-start group">
                  <div className="w-1 h-12 bg-[#3CAA35] rounded-full mt-1 group-hover:h-16 transition-all duration-300"></div>
                  <div>
                    <h3 className="text-2xl font-bold text-[#041E42]">
                      Creer
                    </h3>
                    <p className="text-slate-600 text-lg mt-1 leading-snug">
                      es recuperar claridad sobre el potencial real de tu negocio.
                    </p>
                  </div>
                </div>

                {/* Ítem 2: CREAR */}
                <div className="flex gap-4 items-start group">
                  <div className="w-1 h-12 bg-[#3CAA35] rounded-full mt-1 group-hover:h-16 transition-all duration-300"></div>
                  <div>
                    <h3 className="text-2xl font-bold text-[#041E42]">
                      Crear
                    </h3>
                    <p className="text-slate-600 text-lg mt-1 leading-snug">
                      es construir criterio, estructura y método alineados a tu momento.
                    </p>
                  </div>
                </div>

                {/* Ítem 3: CRECER */}
                <div className="flex gap-4 items-start group">
                  <div className="w-1 h-12 bg-[#3CAA35] rounded-full mt-1 group-hover:h-20 transition-all duration-300"></div>
                  <div>
                    <h3 className="text-2xl font-bold text-[#041E42]">
                      Crecer
                    </h3>
                    <p className="text-slate-600 text-lg mt-1 leading-snug">
                      es tomar decisiones estratégicas que el algoritmo acompaña y que tu negocio puede sostener en el tiempo.
                    </p>
                  </div>
                </div>

              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  );
};

export default Philosophy;