import React from "react";
import { StyleSheet, View } from "react-native";
import { WinrateEloTable } from "../Components/SeasonSeven/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Season 7 (4/4/24 - 6/27/24)</h1>
      <h2 style={{ textAlign: "center" }}>
        <p>
          ELO and Winrates (Players with min 4 drafts shown, min 12 drafts to be
          in awards contention). Last Updated 6/27/24
        </p>
        <p>Winrate Champion and Trophies Champion Matt</p>
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
