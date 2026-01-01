import React, { useState, useEffect } from 'react';
import { Menu, X, Calendar } from 'lucide-react';

const Header: React.FC = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  // Definimos los items del menú con su ID correspondiente (sin tildes para evitar errores)
  const navItems = [
    { label: 'Método', id: 'metodo' },
    { label: 'Programas', id: 'programas' },
    { label: 'Resultados', id: 'resultados' },
    { label: 'FAQ', id: 'faq' },
  ];

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsMobileMenuOpen(false);
    } else {
      console.warn(`No se encontró la sección con id: ${id}`);
    }
  };

  return (
    <header 
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? 'bg-white/95 backdrop-blur-md shadow-sm py-3' : 'bg-transparent py-5'
      }`}
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center">
          
          {/* LOGO */}
          <div className="flex-shrink-0 cursor-pointer" onClick={() => scrollToSection('hero')}>
            <img 
              src="https://i.ibb.co/gLh4Xt72/logo-creseller-fondo-transparente-ISOLOGO.png" 
              alt="Creseller Logo" 
              className="h-[85px] w-auto object-contain" 
            />
          </div>

          {/* Navegación Desktop */}
          <nav className="hidden md:flex items-center gap-8">
            {navItems.map((item) => (
              <button
                key={item.label}
                onClick={() => scrollToSection(item.id)}
                className="text-sm font-bold text-[#041E42] hover:text-[#3CAA35] transition-colors uppercase tracking-wide"
              >
                {item.label}
              </button>
            ))}
            
            {/* BOTÓN AGENDAR */}
            <a 
              href="https://calendly.com/fernandokosoy" 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 bg-[#3CAA35] text-white px-6 py-2.5 rounded-lg font-bold text-sm hover:bg-[#2b7d26] transition-all shadow-lg shadow-green-200 hover:shadow-green-300 transform hover:-translate-y-0.5"
            >
              <Calendar className="w-4 h-4" />
              Agendar Diagnóstico
            </a>
          </nav>

          {/* Botón Menú Móvil */}
          <button 
            className="md:hidden p-2 text-[#041E42]"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X /> : <Menu />}
          </button>
        </div>
      </div>

      {/* Menú Móvil Desplegable */}
      {isMobileMenuOpen && (
        <div className="md:hidden absolute top-full left-0 right-0 bg-white border-t border-slate-100 shadow-lg p-4 flex flex-col gap-4">
          {navItems.map((item) => (
            <button
              key={item.label}
              onClick={() => scrollToSection(item.id)}
              className="text-left py-2 text-[#041E42] font-bold border-b border-slate-50 last:border-0"
            >
              {item.label}
            </button>
          ))}
          <a 
            href="https://calendly.com/fernandokosoy"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-center gap-2 bg-[#3CAA35] text-white px-6 py-3 rounded-lg font-bold text-sm w-full"
          >
            <Calendar className="w-4 h-4" />
            Agendar Diagnóstico
          </a>
        </div>
      )}
    </header>
  );
};

export default Header;