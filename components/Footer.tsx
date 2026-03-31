import React from 'react';
import { Calendar, MessageCircle, Linkedin, Instagram } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer>
      
    
      {/* BARRA INFERIOR (Footer Real) - Fondo Blanco */}
      <div className="bg-white border-t border-slate-100 py-12 px-4 sm:px-6 lg:px-8">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-8">
          
          {/* IZQUIERDA: Logo y Texto */}
          <div className="flex flex-col md:flex-row items-center gap-6 text-center md:text-left">
            {/* Logo Creseller */}
            <img 
              src="https://i.ibb.co/gLh4Xt72/logo-creseller-fondo-transparente-ISOLOGO.png" 
              alt="Creseller Logo" 
              className="h-10 w-auto" 
            />
            
            <div className="hidden md:block w-px h-8 bg-slate-200"></div>
            
            <span className="text-slate-500 text-sm font-medium">
              Consultor de Mercado Libre Certificado
            </span>
          </div>

          {/* CENTRO: Copyright */}
          <div className="text-slate-400 text-sm text-center">
            © 2026 Creseller. Todos los derechos reservados.
          </div>

          {/* DERECHA: Redes Sociales */}
          <div className="flex items-center gap-4">
            <a 
              href="https://www.linkedin.com/in/fernando-kosoy-800b052a/" 
              target="_blank" 
              rel="noopener noreferrer"
              className="p-2 text-slate-400 hover:text-[#041E42] hover:bg-slate-50 rounded-full transition-all"
              aria-label="LinkedIn"
            >
              <Linkedin className="w-6 h-6" />
            </a>
            <a 
              href="#" // Agrega tu Instagram si tienes
              target="_blank" 
              rel="noopener noreferrer"
              className="p-2 text-slate-400 hover:text-[#C13584] hover:bg-slate-50 rounded-full transition-all"
              aria-label="Instagram"
            >
              <Instagram className="w-6 h-6" />
            </a>
            
            {/* Badge País (AR) */}
            <div className="bg-slate-100 text-slate-500 font-bold text-xs px-2 py-1 rounded">
              AR
            </div>
          </div>

        </div>
      </div>
    </footer>
  );
};

export default Footer;
