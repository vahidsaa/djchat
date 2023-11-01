import { ChevronLeft, ChevronRight } from "@mui/icons-material";
import { Box, IconButton } from "@mui/material"
import React from "react";

type Props = {
    open: boolean;
    handelDrawOpen: () => void;
    handelDrawClose: () => void;
};

const DrawerToggle: React.FC<Props> = ({open, handelDrawClose, handelDrawOpen}) => {
    return (
        <Box  sx={{height: "50px", display: "flex", alignItems: "center", justifyContent: "end",}}>
            <IconButton onClick={open ? handelDrawClose : handelDrawOpen}>
              {open ?  <ChevronRight /> : <ChevronLeft />}
            </IconButton>
        </Box>
    );
};

export default DrawerToggle;