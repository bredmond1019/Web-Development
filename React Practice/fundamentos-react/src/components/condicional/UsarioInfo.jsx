import React from "react";
import If, { Else } from "./If";

const UsarioInfo = (props) => {
  const user = props.user || {};
  return (
    <div>
      <If test={user && user.name}>
        Seja bem vindo, <span>{user.name}</span>!
        <Else>
          Seja bem vindo <span>Amigao!</span>
        </Else>
      </If>
    </div>
  );
};

export default UsarioInfo;
