import React from "react";
import "./Contador.css";

import Display from "./Display";
import Botoes from "./Botoes";
import PassoForm from "./PassoForm";

class Contador extends React.Component {
  //   constructor(props) {
  //     super(props);

  //     this.state = {
  //       num: props.numeroInicial,
  //     };
  //   }

  state = {
    num: this.props.numeroInicial || 0,
    pass: this.props.passoInicial || 2,
  };

  inc = () => {
    this.setState({
      num: this.state.num + this.state.pass,
    });
  };

  dec = () => {
    this.setState({
      num: this.state.num - this.state.pass,
    });
  };

  setPass = (novoPasso) => {
    this.setState({
      pass: novoPasso,
    });
  };

  render() {
    return (
      <div className="Contador">
        <h2>Contador</h2>
        <Display num={this.state.num} />
        <PassoForm pass={this.state.pass} setPass={this.setPass} />
        <Botoes setInc={this.inc} setDec={this.dec} />
      </div>
    );
  }
}

export default Contador;
