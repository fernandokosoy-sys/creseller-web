import React from 'react';
import { Search, Users, Settings, TrendingUp } from 'lucide-react';

const Method: React.FC = () => {
  const steps = [
    {
      number: '01',
      title: 'Diagnóstico',
      description: 'Analizamos la salud actual de tu cuenta para identificar frenos y oportunidades reales.',
      icon: Search,
    },
    {
      number: '02',
      title: 'Mentoría + Estrategia',
      description: 'Diseñamos un plan de acción a medida y te acompañamos a definir el rumbo.',
      icon: Users,
    },
    {
      number: '03',
      title: 'Implementación',
      description: 'Ajustamos la operación y aplicamos las correcciones necesarias en tiempo real.',
      icon: Settings,
    },
    {
      number: '04',
      title: 'Escalado',
      description: 'Con las bases sólidas, aceleramos el crecimiento para sostenerlo en el tiempo.',
      icon: TrendingUp,
    },
  ];

  return (
    // CAMBIO CLAVE: Fondo Azul Oscuro (#041E42) para dar fuerza
    <section id="metodo" className="py-24 bg-[#041E42]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Encabezado (Texto Blanco para contrastar) */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <span className="text-[#3CAA35] font-bold tracking-widest uppercase text-sm bg-white/10 px-4 py-1 rounded-full">
            Nuestro Proceso
          </span>
          <h2 className="mt-6 text-4xl font-extrabold text-white sm:text-5xl">
            El método Creseller
          </h2>
          <p className="mt-6 text-xl text-slate-300 leading-relaxed max-w-2xl mx-auto">
            Un acompañamiento estratégico para alinear tu cuenta al algoritmo, ordenar la operación y tomar mejores decisiones.
          </p>
        </div>

        {/* Grilla de Pasos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {steps.map((step) => (
            <div key={step.number} className="bg-white rounded-2xl p-8 relative overflow-hidden group hover:-translate-y-2 transition-transform duration-300">
              
              {/* Borde superior verde decorativo */}
              <div className="absolute top-0 left-0 w-full h-1.5 bg-[#3CAA35]"></div>

              {/* Número grande gris suave de fondo */}
              <span className="absolute -right-2 -top-2 text-7xl font-bold text-slate-100 select-none z-0">
                {step.number}
              </span>
              
              <div className="relative z-10">
                {/* Ícono */}
                <div className="w-14 h-14 bg-[#3CAA35]/10 rounded-xl flex items-center justify-center mb-6">
                  <step.icon className="w-7 h-7 text-[#3CAA35]" />
                </div>
                
                {/* Título */}
                <h3 className="text-xl font-bold text-[#041E42] mb-3">
                  {step.title}
                </h3>
                
                {/* Descripción */}
                <p className="text-slate-600 text-sm leading-relaxed font-medium">
                  {step.description}
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Method;