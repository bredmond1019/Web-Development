import "./App.css";
import React from "react";

import UsarioInfo from "./components/condicional/UsarioInfo";
import EvenOrOdd from "./components/condicional/EvenOrOdd";
import TabelaProdutos from "./components/repeticao/TabelaProdutos";
import ListaAlunos from "./components/repeticao/ListaAlunos";
import FamiliaMembro from "./components/basicos/FamiliaMembro";
import Familia from "./components/basicos/Familia";
import Aleatorio from "./components/basicos/Aleatorio";
import Card from "./components/layout/Card";

const App = (props) => {
  return (
    <div className="App">
      <h1>Fundamentos React</h1>

      <div className="Cards">
        <Card titulo="06 - Renderizacao Condicional" color="#982395">
          <EvenOrOdd num={20}></EvenOrOdd>
          <UsarioInfo user={{ nome: "Brandon" }}></UsarioInfo>
          {/* <UsarioInfo user={{ email: "bredmond1019@gmail.com" }}></UsarioInfo>
          <UsarioInfo></UsarioInfo> */}
        </Card>

        <Card titulo="05 - Repeticao" color="#3A9AD9">
          <TabelaProdutos></TabelaProdutos>
        </Card>

        <Card titulo="04 - Repeticao" color="#FF4C65">
          <ListaAlunos></ListaAlunos>
        </Card>

        <Card titulo="03 - Componente com Filhos" color="#00C8F8">
          <Familia lastname="Redmond">
            <FamiliaMembro name="Brandon" />
            <FamiliaMembro name="Felipe" />
            <FamiliaMembro name="Bella" />
          </Familia>
        </Card>

        <Card titulo="02 - Desafio Aleatorio" color="#080">
          <Aleatorio min={1} max={10} />
        </Card>

        <Card titulo="01 - Desafio Aleatorio">
          <Aleatorio min={1} max={10} />
        </Card>
      </div>
    </div>
  );
};

export default App;
