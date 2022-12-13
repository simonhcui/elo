import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/SeasonOne/TrophiesTable";
import { WinrateEloTable } from "../Components/SeasonOne/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Season 1 (5/6/2022 - 12/9/22)</h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 12/9/22
      </h2>
      <div>
        <View style={styles.container}>
          <WinrateEloTable />
          <TrophiesTable />
        </View>
      </div>
    </>
  );
};

export default SeasonOne;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "space-around",
  },
});
