import React from "react";
import If, { Else } from "./If";

const UsarioInfo = (props) => {
  const user = props.user || {};
  return (
    <div>
      <If test={user && user.name}>
        Seja bem vindo, {user.name}!<Else>Seja bem vindo Amigao</Else>
      </If>
    </div>
  );
};

export default UsarioInfo;
