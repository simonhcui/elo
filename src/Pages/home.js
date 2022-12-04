import React from "react";
import { StyleSheet, View } from "react-native";
import { Table } from "../Components/HomePage/EloTable";
import { WinrateTable } from "../Components/HomePage/WinrateTable";
import { TrophiesTable } from "../Components/HomePage/TrophiesTable";

const Home = () => {
  return (
    <>
      <h1 style={{ textAlign: "center" }}>Simon LGS Stats</h1>
      <h2 style={{ textAlign: "center" }}>
        ELO and Winrates (Min 4 drafts). Last Updated 12/3/22
      </h2>
      <div>
        <View style={styles.container}>
          <Table />
          <WinrateTable />
          <TrophiesTable />
        </View>
      </div>
    </>
  );
};

export default Home;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    justifyContent: "center",
  },
});
