import React from "react";
import { StyleSheet, View } from "react-native";
import { TrophiesTable } from "../Components/Lifetime/TrophiesTable";
import { WinrateEloTable } from "../Components/Lifetime/WinrateEloTable";

const SeasonOne = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Lifetime Stats</h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 12/9/22. Too lazy to
        update currently
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
