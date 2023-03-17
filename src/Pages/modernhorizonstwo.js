import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/ModernHorizonsTwo/MH2TrophiesTable";
import { WinrateTable } from "../Components/ModernHorizonsTwo/MH2WinrateTable";

const ModernHorizonsTwo = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>
        Modern Horizons 2 Stats (13 Drafts Total)
      </h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 3/9/22
      </h2>
      <h2 style={{ textAlign: "center" }}>
        Missing tables due to needing more data. Need More Archetypes to be
        played at least 5 times.
      </h2>
      <div>
        <View style={styles.container}>
          {/* <View style={stylesTwo.container}>
            <ColorTable />
            <Table />
          </View> */}

          <WinrateTable />
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
