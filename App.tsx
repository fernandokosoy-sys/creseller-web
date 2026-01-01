
import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import Philosophy from './components/Philosophy';
import Method from './components/Method';
import Programs from './components/Programs';
import About from './components/About';
import Ecosystem from './components/Ecosystem';
import Results from './components/Results';
import FAQ from './components/FAQ';
import CTASection from './components/CTASection';
import Footer from './components/Footer';

const App: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main>
        <Hero />
        <Philosophy />
        <div id="metodo">
          <Method />
        </div>
        <div id="programas">
          <Programs />
        </div>
        <About />
        <Ecosystem />
        <div id="resultados">
          <Results />
        </div>
        <div id="faq">
          <FAQ />
        </div>
        <CTASection />
      </main>
      <Footer />
    </div>
  );
};

export default App;
