import React from 'react';
import { MessageCircle } from 'lucide-react';
import { WHATSAPP_URL } from './whatsapp';

const WhatsAppButton: React.FC = () => (
  <a
    href={WHATSAPP_URL}
    target="_blank"
    rel="noopener noreferrer"
    aria-label="Escribinos por WhatsApp"
    className="fixed bottom-5 right-5 z-50 bg-green-500 hover:bg-green-600 text-white p-4 rounded-full shadow-xl transition-all"
  >
    <MessageCircle className="w-7 h-7" />
  </a>
);

export default WhatsAppButton;
