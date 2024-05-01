import React from "react";
import { StyleSheet, View } from "react-native";
import { WinrateEloTable } from "../Components/Chaos/WinrateEloTable";

const ModernHorizonsTwo = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Chaos Stats (54 Drafts Total)</h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 4/27/24
      </h2>
      <h2 style={{ textAlign: "center" }}></h2>
      <div>
        <View style={styles.container}>
          <WinrateEloTable />
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
