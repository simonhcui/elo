import React from "react";
import { StyleSheet, View } from "react-native";
import { WinrateEloTable } from "../Components/SeasonFive/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Season 5 (10/5/23 - 12/28/23)</h1>
      <h2 style={{ textAlign: "center" }}>
        <p>
          ELO and Winrates (Players with min 4 drafts shown, min 12 drafts to be
          in awards contention). Last Updated 12/28/23
        </p>
        <p>Winrate Champion and Trophies Champion Chris A</p>
      </h2>
      <div>
        <View style={styles.container}>
          <WinrateEloTable />
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
