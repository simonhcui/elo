import React from "react";
import { useState } from "react";
import { StyleSheet, View } from "react-native";
import BarChart from "../Components/2x2ColorBarChart";
import { Colors } from "../Components/2x2ColorData";
import { TrophiesTable } from "../Components/2x2TrophiesTable";
import { Table } from "../Components/2x2ArchetypeTable";

const DoubleMasters = () => {
  const [userData, setUserData] = useState({
    labels: Colors.map((data) => data.color),
    datasets: [
      {
        label: "Color Winrates",
        data: Colors.map((data) => data.winrate),
        backgroundColor: ["white", "blue", "black", "red", "green"],
        borderColor: "black",
        borderWidth: 2,
      },
    ],
  });

  // const [archetypeData, setArchetypeData] = useState({
  //   labels: Archetypes.map((data) => data.archetype),
  //   datasets: [
  //     {
  //       label: "Archetype Winrates",
  //       data: Archetypes.map((data) => data.winrate),
  //       backgroundColor: [
  //         "0176A7", // 4c no Red
  //         "BDBAB7", // Esper
  //         "96B551", // Selesnya
  //         "A46110", // 5c
  //         "11103A", // Grixis
  //         "BC0515", // Boros
  //         "723A1D", // Abzan
  //         "B0553B", // Mardu
  //         "6A891E", // Jund
  //         "312C2D", // 4c no White
  //         "005964", // Sultai
  //         "C1B4CD", // Jeskai
  //         "ED5611", // Naya
  //         "00BC98", // Bant
  //       ],
  //       borderColor: "black",
  //       borderWidth: 2,
  //     },
  //   ],
  // });

  return (
    <>
      <h1 style={{ textAlign: "center" }}>
        Double Masters 2022 Stats (19 Drafts Total)
      </h1>
      <View style={styles.container}>
        <div style={{ width: 700 }}>
          <View style={{ flex: 1 }}>
            <BarChart chartData={userData} />
          </View>
        </div>
        <div style={{ paddingLeft: 100 }}>
          <View style={{ flex: 4 }}>
            <Table />
          </View>
        </div>
        <TrophiesTable />
      </View>
      {/* <Table />
      <View style={{ innerWidth: 400 }}>
        <BarChart chartData={userData} />
      </View> */}
    </>
  );
};

export default DoubleMasters;

const styles = StyleSheet.create({
  container: {
    flexDirection: "row",
    flex: 1,
    justifyContent: "space-around",
  },
});
