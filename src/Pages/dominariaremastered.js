import React from "react";
import { StyleSheet, View } from "react-native";
//import { TrophiesTable } from "../Components/ModernHorizonsTwo/MH2TrophiesTable";
//import { WinrateTable } from "../Components/ModernHorizonsTwo/MH2WinrateTable";
import { Table } from "../Components/DominariaRemastered/DMRArchetypeTable";
import { ColorTable } from "../Components/DominariaRemastered/DMRColorTable";
import { WinrateEloTable } from "../Components/DominariaRemastered/WinrateEloTable";

const ModernHorizonsTwo = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>
        Dominaria Remastered Stats (18 Drafts Total)
      </h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 5 drafts). Last Updated 4/5/24
      </h2>
      <h2 style={{ textAlign: "center" }}></h2>
      <div>
        <View style={styles.container}>
          <View style={stylesTwo.container}>
            <ColorTable />
            <Table />
          </View>

          <WinrateEloTable />
          {/* <WinrateTable /> */}
          {/* <EloTable /> */}
          {/* <TrophiesTable /> */}
        </View>
      </div>
    </>
  );
};

export default ModernHorizonsTwo;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "center",
  },
});

const stylesTwo = StyleSheet.create({
  container: {
    flexDirection: "column",
    justifyContent: "flex-start",
  },
});
