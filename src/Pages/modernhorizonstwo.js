import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/ModernHorizonsTwo/MH2TrophiesTable";
import { WinrateTable } from "../Components/ModernHorizonsTwo/MH2WinrateTable";
import { Table } from "../Components/ModernHorizonsTwo/MH2ArchetypeTable";
import { WinrateEloTable } from "../Components/ModernHorizonsTwo/WinrateEloTable";

const ModernHorizonsTwo = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>
        Modern Horizons 2 Stats (17 Drafts Total)
      </h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 5/13/23
      </h2>
      <h2 style={{ textAlign: "center" }}></h2>
      <div>
        <View style={styles.container}>
          <View style={stylesTwo.container}>
            {/* <ColorTable /> */}
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
