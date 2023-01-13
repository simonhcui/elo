import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/DoubleMasters/2x2TrophiesTable";
import { Table } from "../Components/DoubleMasters/2x2ArchetypeTable";
import { EloTable } from "../Components/DoubleMasters/2x2EloTable";
import { WinrateTable } from "../Components/DoubleMasters/2x2WinrateTable";
import { ColorTable } from "../Components/DoubleMasters/2x2ColorTable";
import { WinrateEloTable } from "../Components/DoubleMasters/WinrateEloTable";

const DoubleMasters = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>
        Double Masters 2022 Stats (22 Drafts Total)
      </h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 1/12/23
      </h2>
      <div>
        <View style={styles.container}>
          <View style={stylesTwo.container}>
            <ColorTable />
            <Table />
          </View>

          <WinrateEloTable />
          {/* <WinrateTable />
          <EloTable /> */}
          <TrophiesTable />
        </View>
      </div>
    </>
  );
};

export default DoubleMasters;

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
